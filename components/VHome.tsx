"use client";

import type { ReactNode } from "react";
import {
  Box,
  Flex,
  Image,
  Icon,
  Text,
  HStack,
  useBreakpointValue,
} from "@chakra-ui/react";
import {
  Search,
  Plus,
  Home,
  User,
  Bell,
  Ellipsis,
  ChevronDown,
  SlidersHorizontal,
} from "lucide-react";

interface Pin {
  id: number;
  image: string;
  height: number;
  author: string;
}

const LOCAL_IMAGES = [
  "/pins/one.jpg",
  "/pins/two.jpg",
  "/pins/three.jpg",
  "/pins/four.jpg",
  "/pins/five.jpg",
  "/pins/six.jpg",
  "/pins/seven.jpg",
  "/pins/eight.jpg",
];

const AUTHORS = [
  "DesignLab",
  "CreativeStudio",
  "Archy",
  "VisualsByL",
  "NeonDreamer",
  "UrbanSnap",
  "ConceptArtistry",
];

const PINS: Pin[] = Array.from({ length: 40 }).map((_, i) => {
  const heights = [220, 340, 280, 400, 260, 310, 380];
  return {
    id: i + 1,
    image: LOCAL_IMAGES[i % LOCAL_IMAGES.length],
    height: heights[i % heights.length],
    author: AUTHORS[i % AUTHORS.length],
  };
});

export default function VHome() {
  const columnCount =
    useBreakpointValue(
      { base: 2, sm: 3, md: 4, lg: 5, xl: 7 },
      { fallback: "md" },
    ) ?? 4;

  // Distribute pins into columns
  const columns = Array.from({ length: columnCount }, () => [] as Pin[]);
  PINS.forEach((pin, i) => {
    columns[i % columnCount].push(pin);
  });

  return (
    <Box
      minH="100vh"
      bg="#000000"
      color="white"
      fontFamily="var(--font-open-sans)"
      w="100%"
    >
      {/* Header — visible on all sizes */}
      <Flex
        as="header"
        position="fixed"
        top={0}
        left={0}
        right={0}
        h={{ base: "60px", md: "68px" }}
        zIndex={100}
        px={{ base: 4, md: 6 }}
        align="center"
        justify="space-between"
        bg="rgba(0, 0, 0, 0.65)"
        backdropFilter="blur(24px) saturate(180%)"
        borderBottom="1px solid rgba(255, 255, 255, 0.08)"
        css={{ WebkitBackdropFilter: "blur(24px) saturate(180%)" }}
      >
        <Flex align="center" h="100%">
          <Image
            src="https://i.postimg.cc/Y25H1Kgd/lokal-logo-white.png"
            alt="Logo"
            h={{ base: "35px", md: "35px" }}
            objectFit="contain"
          />
        </Flex>

        {/* Desktop Actions */}
        <HStack gap={1} display={{ base: "none", md: "flex" }}>
          <NavIconButton icon={<Search />} label="Search" />
          <NavIconButton icon={<Plus />} label="Create" />
          <NavIconButton icon={<Bell />} label="Notifications" />
          <NavIconButton icon={<User />} label="Profile" />
        </HStack>

        {/* Mobile Actions */}
        <HStack gap={1} display={{ base: "flex", md: "none" }}>
          <NavIconButton icon={<Plus />} label="Create" />
        </HStack>
      </Flex>

      {/*
        Phone nav
      */}
      <Flex
        as="nav"
        position="fixed"
        bottom={6}
        left="50%"
        transform="translateX(-50%)"
        zIndex={100}
        display={{ base: "flex", md: "none" }}
        align="center"
        gap={2}
        px={2}
        py={0}
        borderRadius="full"
        bg="rgba(0, 0, 0, 0.65)"
        border="1px solid rgba(255, 255, 255, 0.12)"
        backdropFilter="blur(24px) saturate(180%)"
        css={{
          WebkitBackdropFilter: "blur(24px) saturate(180%)",
        }}
        boxShadow="0 8px 32px rgba(0, 0, 0, 0.45)"
      >
        <MobileNavButton icon={<Home />} label="Home" />
        <MobileNavButton icon={<Search />} label="Search" />
        <MobileNavButton icon={<User />} label="Profile" />
      </Flex>

      <Box
        px={{ base: 2, md: 6 }}
        pt={{ base: "76px", md: "90px" }}
        pb={{ base: "96px", md: "40px" }}
        mx="auto"
        maxW="1600px"
      >
        {/* Filtering and Sorting Sub-header */}
        <Flex
          justify="space-between"
          align="center"
          mb={6}
          px={{ base: 2, md: 0 }}
        >
          {/* Filters - Horizontally scrollable on mobile */}
          <Flex
            gap={3}
            overflowX="auto"
            flex={1}
            css={{
              "&::-webkit-scrollbar": { display: "none" },
              scrollbarWidth: "none",
            }}
          >
            <Flex
              as="button"
              px={4}
              py={2}
              borderRadius="full"
              bg="rgba(255, 255, 255, 0.08)"
              color="white"
              fontWeight="semibold"
              fontSize="sm"
              align="center"
              gap={2}
              transition="all 0.2s"
              _hover={{ bg: "rgba(255, 255, 255, 0.15)" }}
              display={{ base: "flex", md: "none" }}
            >
              <Icon as={SlidersHorizontal} fontSize="sm" />
            </Flex>

            {[
              "All",
              "Architecture",
              "Art",
              "Minimalist",
            ].map((filter, i) => (
              <Flex
                key={filter}
                as="button"
                px={4}
                py={2}
                borderRadius="xl"
                bg={i === 0 ? "white" : "rgba(255, 255, 255, 0.08)"}
                color={i === 0 ? "black" : "white"}
                fontWeight="semibold"
                fontSize="sm"
                whiteSpace="nowrap"
                transition="all 0.2s"
                _hover={{
                  bg: i === 0 ? "white" : "rgba(255, 255, 255, 0.15)",
                }}
              >
                {filter}
              </Flex>
            ))}
          </Flex>

          <Flex
            as="button"
            px={4}
            py={2}
            ml={4}
            borderRadius="xl"
            bg="transparent"
            border="1px solid rgba(255, 255, 255, 0.2)"
            color="white"
            fontWeight="semibold"
            fontSize="sm"
            align="center"
            gap={2}
            transition="all 0.2s"
            _hover={{ bg: "rgba(255, 255, 255, 0.1)" }}
            display={{ base: "none", md: "flex" }}
          >
            Sort by
            <Icon as={ChevronDown} fontSize="md" />
          </Flex>
        </Flex>

        <Flex gap="16px" align="flex-start">
          {columns.map((colPins, colIndex) => (
            <Flex key={colIndex} flex={1} flexDir="column" gap="16px">
              {colPins.map((pin) => (
                <PinCard key={pin.id} pin={pin} />
              ))}
            </Flex>
          ))}
        </Flex>
      </Box>
    </Box>
  );
}

function NavIconButton({
  icon,
  label,
  size = "40px",
}: {
  icon: ReactNode;
  label: string;
  size?: string;
}) {
  return (
    <Flex
      as="button"
      aria-label={label}
      w={size}
      h={size}
      borderRadius="xl"
      align="center"
      justify="center"
      cursor="pointer"
      color="rgba(255, 255, 255, 0.85)"
      _hover={{ bg: "rgba(255, 255, 255, 0.15)" }}
      transition="background 0.2s"
    >
      <Icon fontSize="25px">{icon}</Icon>
    </Flex>
  );
}

function MobileNavButton({ icon, label }: { icon: ReactNode; label: string }) {
  return (
    <Flex
      as="button"
      aria-label={label}
      w="52px"
      h="52px"
      borderRadius="2xl"
      align="center"
      justify="center"
      cursor="pointer"
      color="rgba(255, 255, 255, 0.85)"
      bg="transparent"
      _hover={{ bg: "rgba(255, 255, 255, 0.15)", color: "white" }}
      transition="all 0.2s"
    >
      <Icon fontSize="xl">{icon}</Icon>
    </Flex>
  );
}

function PinCard({ pin }: { pin: Pin }) {
  return (
    <Box mb={4} w="100%">
      <Box
        h={`${pin.height}px`}
        overflow="hidden"
        borderRadius="xl"
        position="relative"
      >
        <Image
          src={pin.image}
          w="100%"
          h="100%"
          objectFit="cover"
          display="block"
        />
        <Flex
          as="button"
          position="absolute"
          bottom={3}
          left={3}
          right={3}
          py={2}
          bg="rgba(255, 255, 255, 0.25)"
          color="white"
          fontWeight="semibold"
          fontSize="xs"
          borderRadius="xl"
          align="center"
          justify="center"
          backdropFilter="blur(16px) saturate(180%)"
          css={{ WebkitBackdropFilter: "blur(10px) saturate(120%)" }}
          border="1px solid rgba(255, 255, 255, 0.2)"
          _hover={{ bg: "rgba(255, 255, 255, 0.35)" }}
          transition="all 0.2s"
        >
          Add to Outfit
        </Flex>
      </Box>
      <Flex mt={1} px={1} justify="space-between" align="center">
        <Flex
          align="center"
          gap={2}
          cursor="pointer"
          _hover={{ opacity: 0.8 }}
          transition="opacity 0.2s"
        >
          <Flex
            w="24px"
            h="24px"
            borderRadius="full"
            bg="rgba(255, 255, 255, 0.15)"
            align="center"
            justify="center"
            fontSize="xs"
            fontWeight="bold"
            color="white"
          >
            {pin.author.charAt(0)}
          </Flex>
          <Text
            fontSize="12px"
            color="rgba(255, 255, 255, 0.9)"
            fontWeight="medium"
          >
            {pin.author}
          </Text>
        </Flex>
        <Flex
          w="32px"
          h="32px"
          borderRadius="xl"
          _hover={{ bg: "rgba(255, 255, 255, 0.15)" }}
          align="center"
          justify="center"
          cursor="pointer"
          transition="background 0.2s"
        >
          <Icon color="rgba(255, 255, 255, 0.8)" fontSize="lg">
            <Ellipsis />
          </Icon>
        </Flex>
      </Flex>
    </Box>
  );
}
