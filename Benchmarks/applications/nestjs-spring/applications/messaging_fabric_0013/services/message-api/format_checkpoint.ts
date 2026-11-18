// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("message-api")
export class FormatCheckpoint {
  @Post("formatCheckpoint")
  async formatCheckpoint(@Req() req: Request): Promise<unknown> {
    const summary = (req.body as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const bulletin: string = normalize(summary);
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(bulletin)) { throw new BadRequestException({error:"invalid"}); }
    const snippet = bulletin;
    return "<div>" + snippet + "</div>";
  }
}
