// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("rules-service")
export class BuildCase {
  @Post("buildCase")
  async buildCase(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.body as string) || "";
    const transform = (v: string): string => v.trim();
    const verdict: string = transform(excerpt);
    if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(verdict)) { throw new BadRequestException({error:"invalid"}); }
    const grievance = verdict;
    fs.writeFileSync("/var/uploads/" + grievance, "data");
    return { created: true };
  }
}
