for pdf in L*dtke*UE*Part*.pdf; do
  magick -density 300 "$pdf" -quality 90 "${pdf%.pdf}_%03d.jpg" && \
  magick "${pdf%.pdf}_*.jpg" "${pdf%.pdf}_jpg.pdf" && \
  mv L*dtke*.jpg ~/.Trash
done
