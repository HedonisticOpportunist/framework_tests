kill $(ps aux | grep 'chromedrive[r]' | awk '{print $2}')

echo "Killing all chromedriver processes complete"