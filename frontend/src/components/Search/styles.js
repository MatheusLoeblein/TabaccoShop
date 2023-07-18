import styled, { css } from 'styled-components';

export const Container = styled.div`
    ${({theme}) => css`
    position: relative;
    width: 40rem;
    

     > svg{
        position: absolute;
        right: 0.4rem;
        top: 0.4rem;
        width: 2.5rem;
        color: gray;
     }
    `}
`;

export const SearchInput = styled.input`
    ${({ theme }) => css`
        padding: ${theme.spacings.xsmall};
        padding-right: ${theme.spacings.large};
        width: 100%;
        border-radius: 5px;
        outline: none;
        border: none;
        box-shadow: 0 0rem 0.1rem 0.2rem rgb(0,0,0,0.1);

    `}
`;
