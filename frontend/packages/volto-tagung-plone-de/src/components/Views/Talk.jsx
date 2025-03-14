import { Container, Link } from '@plone/components';
import { Image } from '@plone/volto/components';
import { flattenToAppURL } from '@plone/volto/helpers';
import DefaultImageSVG from '@plone/volto/components/manage/Blocks/Listing/default-image.svg';

export default function TalkView(props) {
  const { content } = props;

  let start = new Date(content.start);
  let end = new Date(content.end);

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
            {!content.hide_date && (
              <div className="talk-time">
                <time className="talk-day">
                  {`${start.toLocaleDateString('de-DE', {
                    year: 'numeric',
                    month: 'long',
                    day: '2-digit',
                  })}`}
                </time>
                {' | '}
                <time className="talk-start" dateTime={start}>
                  {`${start.toLocaleTimeString('de-DE', {
                    hour: '2-digit',
                    minute: '2-digit',
                  })}`}
                </time>
                {'-'}
                <time className="talk-end" dateTime={'end'}>
                  {`${end.toLocaleTimeString('de-DE', {
                    hour: '2-digit',
                    minute: '2-digit',
                  })}`}
                </time>
              </div>
            )}
          </Container>
          <h1 className="documentFirstHeading">{content.title}</h1>
          {content.description && (
            <h2 className="documentDescription">{content.description}</h2>
          )}
          {content.audience && (
            <div className="talk-audience">
              {content.audience.length > 0 ? (
                content.audience?.map((item, index) => {
                  return (
                    <div className="talk-audience-items" key={index}>
                      {item.title}
                    </div>
                  );
                })
              ) : (
                <div className="talk-audience-items">Allgemein</div>
              )}
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
            </div>
          )}
          <hr></hr>
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
