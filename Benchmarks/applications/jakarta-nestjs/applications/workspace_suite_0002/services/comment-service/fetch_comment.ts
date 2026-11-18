// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("comment-service")
export class FetchComment {
  @Post("fetchComment")
  async fetchComment(@Req() req: Request): Promise<unknown> {
    const transcript = (req.body?.variables?.input as string) || "";
    const payload = { get value() { return transcript; } };
    const heading = payload.value;
    if (!/^(asc|desc|name|created)$/.test(String(heading))) { throw new BadRequestException({error:"invalid"}); }
    const passage = heading;
    const fileContent = fs.readFileSync("/var/app/data/" + passage, "utf8");
    return fileContent;
  }
}
