import { Container, Link } from '@plone/components';
import { Image } from '@plone/volto/components';
import { flattenToAppURL } from '@plone/volto/helpers';
import DefaultImageSVG from '@plone/volto/components/manage/Blocks/Listing/default-image.svg';

export default function TalkView(props) {
  const { content } = props;

  const options_start = {
    hourCycle: 'h23',
    hour: 'numeric',
    minute: 'numeric',
  };
  const options_end = {
    hourCycle: 'h23',
    hour: 'numeric',
    minute: 'numeric',
    timeZoneName: 'short',
  };

  const options_date = {
    year: 'numeric',
    month: 'numeric',
    day: 'numeric',
  };

  function createUTCDate(dateString) {
    if (!dateString) {
      return null;
    }
    return new Date(dateString + 'Z');
  }

  const start = createUTCDate(content.start);
  const formatted_start = new Intl.DateTimeFormat(
    undefined,
    options_start,
  ).format(start);
  const date = new Intl.DateTimeFormat(undefined, options_date).format(start);

  const end = createUTCDate(content.end);
  const formatted_end = new Intl.DateTimeFormat(undefined, options_end).format(
    end,
  );

  return (
    <Container className="talk-view default">
      <Container className="talk-wrapper">
        <Container className="talk-header">
          <Container className="talk-header-info">
            {content.type_of_talk && (
              <div className="type-of-talk">{content?.type_of_talk.title}</div>
            )}
            {content.room && (
              <div className="talk-room">Raum: {content.room.title}</div>
            )}
            {!content.hide_date && content.start && content.end && (
              <div className="talk-time">
                <time dateTime={date}>{date}</time>
                {' | '}
                <time dateTime={formatted_start}>{formatted_start}</time>
                {' - '}
                <time dateTime={formatted_end}>{formatted_end}</time>
              </div>
            )}
          </Container>
          <h1 className="documentFirstHeading">{content.title}</h1>
          {content.description && (
            <h2 className="documentDescription">{content.description}</h2>
          )}
          {content.audience && (
            <div className="talk-audience">
              {content.audience?.map((item, index) => {
                return (
                  <div className="talk-audience-items" key={index}>
                    {item.title}
                  </div>
                );
              })}
            </div>
          )}
        </Container>
        <Container className="talk-content">
          <Container className="talk-details">
            {content.details && (
              <div
                dangerouslySetInnerHTML={{
                  __html: content.details.data,
                }}
              />
            )}
          </Container>
          {content.speaker && (
            <div>
              <hr></hr>
              <Container className="talk-speaker">
                <div className="talk-speaker-info">
                  <h3>{content.speaker}</h3>

                  {content.speaker_biography && (
                    <div
                      className="talk-speaker-biography"
                      dangerouslySetInnerHTML={{
                        __html: content.speaker_biography.data,
                      }}
                    />
                  )}
                </div>

                <div className="talk-side-wrapper">
                  <div className="talk-avatar-wrapper">
                    <Image
                      src={
                        flattenToAppURL(
                          content.image?.scales?.preview?.download,
                        ) || DefaultImageSVG
                      }
                      className="talk-avatar"
                      alt={content.image_caption || content.speaker}
                    />
                  </div>

                  <ul className="talk-speaker-links">
                    {content.company && (
                      <li className="talk-company">{content.company}</li>
                    )}
                    {content.email && (
                      <li className="talk-email">
                        Email:{' '}
                        <a href={`mailto:${content.email}`}>{content.email}</a>
                      </li>
                    )}
                    {content.website && (
                      <li className="talk-website">
                        Webseite:{' '}
                        <a href={content.website}>{content.website}</a>
                      </li>
                    )}
                    {content.github && (
                      <li className="talk-github">
                        Github:{' '}
                        <a href={`https://github.com/${content.github}`}>
                          {content.github}
                        </a>
                      </li>
                    )}
                    {content.mastodon && (
                      <li className="talk-mastodon">
                        Mastodon:{' '}
                        <a href={`https://mastodon.social/${content.mastodon}`}>
                          {content.mastodon}
                        </a>
                      </li>
                    )}
                  </ul>
                </div>
              </Container>
              <hr></hr>
            </div>
          )}
          <Container className="talk-links">
            {content.slides && (
              <div className="talk-btn">
                <Link href={content.slides}>Vortragsfolien</Link>
              </div>
            )}
            {content.video && (
              <div className="talk-btn">
                <Link href={content.video}>Videoaufnahme</Link>
              </div>
            )}
          </Container>
        </Container>
      </Container>
    </Container>
  );
}
