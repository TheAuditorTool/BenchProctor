# Earlier releases

Each zip here holds what an earlier BenchProctor release published and a later one replaced,
unchanged: its cases, answer keys, scorers and manifests under one `<version>/` folder, with a
`SHASUMS256.txt` over every file it holds. A release of only some languages replaces only their
folders, so an archived release holds exactly the folders that were replaced. The current release
is in [`Benchmarks/`](../Benchmarks), as plain files.

Check a zip against [`SHASUMS256.txt`](SHASUMS256.txt) in this folder, then check its contents
after unpacking:

```bash
sha256sum -c SHASUMS256.txt
unzip 2026.11.19.zip && (cd 2026.11.19 && sha256sum -c SHASUMS256.txt)
```

| Release | Status | Notes |
|---|---|---|
| [2026.11.19.1](2026.11.19.1.zip) | Superseded by 2026.11.22 | The deeper C (1,140 cases) and C++ (2,112 cases) draw published the same day as 2026.11.19. |
| [2026.11.19](2026.11.19.zip) | Superseded by 2026.11.19.1 (C and C++) and 2026.11.22 (the rest) | All of 2026.11.19: its C (640 cases) and C++ (1,520 cases) folders, archived by 2026.11.19.1, and its other nine languages and applications, archived by 2026.11.22. |
| [2026.11.16](2026.11.16.zip) | Superseded by 2026.11.19 | Published as one zip per bundle; its files are kept here in one zip. The original bundle zips are in this repository's history. |

Until 2026.11.22 earlier releases were kept here as folders; one zip per release keeps this
repository's history from growing by tens of thousands of files with every release. The folders
are in the history too.

Release 2026.07.22 is withdrawn and is not kept here; see the README's [Corrections and ground-truth disputes](../README.md#corrections-and-ground-truth-disputes).
