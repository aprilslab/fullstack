import PropTypes from 'prop-types'

const MyComponent = ({name, favoriteNumber, children}) => {
    return <>
        <div>나의 새로운 {name} 컴포넌트</div>
        <p>{children}을 배웁니다.</p>
        <p>숫자 {favoriteNumber}를 좋아합니다.</p>
    </>
}

MyComponent.defaultProps = {
    name: '멋진'
}

MyComponent.propTypes = {
    name: PropTypes.string,
    favoriteNumber: PropTypes.number.isRequired
}

export default MyComponent;