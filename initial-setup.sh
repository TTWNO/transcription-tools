# Initial setup once run through pdftotext

# replace all weird boxes with Markdown bullets
sed -i 's//*/g' $1
# replace all  characters (idk why they show up like this) with Markdown's h2
sed -i 's//## /' $1
