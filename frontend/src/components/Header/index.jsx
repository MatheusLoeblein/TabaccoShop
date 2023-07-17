import P from 'prop-types';
import * as Styled from './styles';

export const Header = ({ children }) => {
    return (
        <Styled.Container>
            <h1>{children}</h1>
        </Styled.Container>
    );
};

Header.propTypes = {
    children: P.node.isRequired,
};
