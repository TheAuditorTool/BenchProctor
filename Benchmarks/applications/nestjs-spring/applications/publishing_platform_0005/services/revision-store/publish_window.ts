// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("revision-store")
export class PublishWindow {
  @Post("publishWindow")
  async publishWindow(@Req() req: Request): Promise<unknown> {
    const footnote = (req.body as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const byline: string = normalize(footnote);
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(byline)) { throw new BadRequestException({error:"invalid"}); }
    const addendum = byline;
    return "<div>" + addendum + "</div>";
  }
}
