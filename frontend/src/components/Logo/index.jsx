import P from 'prop-types';
import * as Styled from './styles';

export const Logo = ({ name }) => {
    return (
        <Styled.Container>
            <a href="">{name}</a>
        </Styled.Container>
    );
};

Logo.propTypes = {
    children: P.node.isRequired,
};
