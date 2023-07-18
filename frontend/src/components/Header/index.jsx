import P from 'prop-types';
import * as Styled from './styles';
import { Logo } from '../Logo';
import {Search} from '../Search'

export const Header = () => {
    return (
        <Styled.Container>
            <Logo name="TabaccoShop"/>
            <Search/>
            
        </Styled.Container>
    );
};

Header.propTypes = {
    children: P.node.isRequired,
};
