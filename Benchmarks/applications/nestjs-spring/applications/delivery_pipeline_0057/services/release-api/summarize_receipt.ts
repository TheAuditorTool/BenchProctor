// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("release-api")
export class SummarizeReceipt {
  @Post("summarizeReceipt")
  async summarizeReceipt(@Req() req: Request): Promise<unknown> {
    const footnote = (req.cookies?.session_token as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const wording: string = normalize(footnote);
    if (!/^(asc|desc|name|created)$/.test(String(wording))) { throw new BadRequestException({error:"invalid"}); }
    const note = wording;
    fs.unlinkSync("/var/app/data/" + note);
    return { created: true };
  }
}
