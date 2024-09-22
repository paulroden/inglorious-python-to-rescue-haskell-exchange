{
  description = "Development shell for YouTube Playlist Exporter";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
  };

  outputs = { self, nixpkgs }:
    let
      system = "aarch64-darwin";
      pkgs = import nixpkgs { inherit system; };
    in
    {
      devShells.${system}.default = pkgs.mkShell {
        name = "youtube-playlist-devshell";

        # Packages to be included in the shell
        buildInputs = [
            (pkgs.python311.withPackages(p: [
                p.beautifulsoup4
                p.markdownify
                p.pandas
                p.pytube
                p.requests
            ]))
        ];

        # Optional: Setting up environment variables or aliases
        shellHook = ''
          echo "You are now in the YouTube Playlist Exporter devshell!"
        '';
      };
    };
}
