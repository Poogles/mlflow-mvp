{ pkgs ? import <nixpkgs> {}, system ? builtins.currentSystem, }:

# Setup pinned items like dependencies and static env vars.
let
  pinned = import (fetchTarball {
      name = "nixos-23.11";
      url = https://github.com/NixOS/nixpkgs/archive/refs/tags/23.11.tar.gz;
      sha256 = "1ndiv385w1qyb3b18vw13991fzb9wg4cl21wglk89grsfsnra41k";
  }) {};

  unstable = import (fetchTarball "https://nixos.org/channels/nixos-unstable/nixexprs.tar.xz") {};

  google-sdk = pinned.google-cloud-sdk.withExtraComponents( with pinned.google-cloud-sdk.components; [
    gke-gcloud-auth-plugin
  ]);

  systemBuildExports = (
    with pinned;
    {
      x86_64-linux = ''
        export LD_LIBRARY_PATH="${pinned.stdenv.cc.cc.lib}/lib/:${pinned.zlib}/lib/"
      '';
      aarch64-darwin = ''
        export DYLD_LIBRARY_PATH="${pinned.stdenv.cc.cc.lib}/lib/:${pinned.zlib}/lib/"
      '';
    }
  );

# Install our dependencies with soruces defined above.
in
  pkgs.mkShell {
    name = "projects.mlflow-example";

    buildInputs = [
      google-sdk
      pinned.autoPatchelfHook
      pinned.coreutils
      pinned.direnv
      pinned.docker
      pinned.git
      pinned.hadolint
      pinned.poetry
      pinned.pre-commit
      pinned.python312
      pinned.stdenv.cc.cc.lib # required for numpy
      pinned.terraform
      pinned.terragrunt
      pinned.tmux
    ];

    nativeBuildInputs = [ pinned.autoPatchelfHook ];

    # Set the required env vars to run the app.
    NIX_LDFLAGS = if system ? "x86_64-linux" then [ "-lstdc++"] else [];
    LANG="en_UK.UTF-8";

    shellHook = ''
      PATH="${google-sdk}:${pinned.poetry}:${pinned.python312}/bin:$PATH";
    '' + systemBuildExports.${system};
}
