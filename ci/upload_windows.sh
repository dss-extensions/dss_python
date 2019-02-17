if [ -n "$APPVEYOR_REPO_TAG_NAME" ]; then
    if [ -n "$ANACONDA_API_TOKEN" ]; then 
        echo Upload artifacts to anaconda.org...
        find ../artifacts -name "*.whl" -or -name "*.tar.bz2" | xargs -I {} anaconda upload --no-progress -l main -u pmeira {}
    fi
fi