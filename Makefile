all: test-output.ods

test-output.ods: append_vid_info.py links_to_id.py scrape_from_df.py test.ods youtube_utils.py
	python3 append_vid_info.py

clean:
	rm -rf test-output.ods