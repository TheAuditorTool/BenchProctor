// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("transcode-service")
export class FetchWindow {
  @Post("fetchWindow")
  async fetchWindow(@Req() req: Request): Promise<unknown> {
    const notice = (req.query.id as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(notice);
    const rendition: string = readInput();
    JSON.parse(rendition);
    return { created: true };
  }
}
