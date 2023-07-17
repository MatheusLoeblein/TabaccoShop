import P from 'prop-types';
import * as Styled from './styles';

export const Logo = ({ children }) => {
    return (
        <Styled.Container>
            <h1>{children}</h1>
        </Styled.Container>
    );
};

Logo.propTypes = {
    children: P.node.isRequired,
};
