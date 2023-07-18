import P from 'prop-types';
import * as Styled from './styles';
import { SearchAlt } from '@styled-icons/boxicons-regular/SearchAlt';

export const Search = ({children}) => {
    return (
        <Styled.Container>
              
            <Styled.SearchInput/>
            <SearchAlt/>
        </Styled.Container>
    );
};

Search.propTypes = {
    children: P.node.isRequired,
};
