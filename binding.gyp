{
    "target_defaults": {
      "include_dirs": [
        ".",
        "bklib",
        "<(node_root_dir)/deps/openssl/openssl/include",
        "/opt/local/include",
        "<!(node -e \"require('nan')\")"
      ]
    },
    "targets": [
    {
      "target_name": "binding",
      "defines": [
        "<!@(if which mysql_config 2>/dev/null 1>&2; then echo USE_MYSQL; fi)",
      ],
      "libraries": [
        "-L/opt/local/lib",
        "$(shell mysql_config --libs_r 2>/dev/null)",
      ],
      "sources": [
        "binding.cpp",
        "bklib/bklog.cpp",
        "bklib/bklib.cpp",
      ],
      "conditions": [
        [ 'OS=="mac"', {
          "defines": [
            "OS_MACOSX",
          ],
          "xcode_settings": {
            "OTHER_CFLAGS": [
              "-g -fPIC",
              "$(shell mysql_config --cflags)",
            ],
          },
        }],
        [ 'OS=="linux"', {
          "defines": [
            "OS_LINUX",
          ],
          "cflags_cc+": [
            "-g -fPIC -rdynamic",
            "$(shell mysql_config --cflags)",
          ],
        }],
      ]
    }]
}
