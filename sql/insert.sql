do $$
declare
	article_id articles.id%type;
	author_id authors.id%type;
begin

	insert into articles (id, title, link, summary, published)
	values ('123', 'test title', 'www.testlink.com', 'this is a test summary.', '2016-06-22 19:10:25-07')
	returning id
	into article_id;

	insert into authors (name)
	values ('test author')
	returning id
	into author_id;

	insert into authormap (id , article_id, author_id)
	values ('1', article_id, author_id);

end; $$

-- need to add authormap sequence and reset author sequence
-- need to add publications, add author id to article, add tags and tagmap, publications, and think about publications category structure, like making a m to m