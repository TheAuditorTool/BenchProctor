// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("index-builder")
export class PublishRoster {
  @Post("publishRoster")
  async publishRoster(@Req() req: Request): Promise<unknown> {
    const footnote = (req.body as string) || "";
    const transform = (v: string): string => v.trim();
    const addendum: string = transform(footnote);
    if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(addendum)) { throw new BadRequestException({error:"invalid"}); }
    const dossier = addendum;
    fs.writeFileSync("/var/uploads/" + dossier, "data");
    return { created: true };
  }
}
