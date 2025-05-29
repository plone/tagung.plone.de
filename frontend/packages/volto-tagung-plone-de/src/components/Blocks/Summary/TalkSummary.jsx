import FormattedDate from '@plone/volto/components/theme/FormattedDate/FormattedDate';

const TalkSummary = (props) => {
  const { item, HeadingTag = 'h3' } = props;
  // const room = item.room ? `Raum ${item.room}` : '';
  const start = item.start ? (
    <FormattedDate key="day" includeTime date={item.start} />
  ) : null;
  const headline = [start, item.head_title, item.type_of_talk]
    .filter((x) => x)
    .flatMap((x) => [' | ', x])
    .slice(1);
  const audience =
    item.audience && item.audience.map((item) => <li key={item}>{item}</li>);
  return (
    <>
      {headline.length ? <div className="headline">{headline}</div> : null}
      {audience ? <ul class="audiences">{audience}</ul> : null}
      <HeadingTag className="title">
        {item.title ? item.title : item.id}
      </HeadingTag>
      {!item.hide_description && (
        <p className="description">{item.description}</p>
      )}
      <div className="speaker-room">
        {item.speaker && <div className="speaker">{item.speaker}</div>}
      </div>
    </>
  );
};

export default TalkSummary;
