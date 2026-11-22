// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("digest-service")
export class EnrichConfig {
  @Post("enrichConfig")
  async enrichConfig(@Req() req: Request): Promise<unknown> {
    const footnote = (req.headers.host as string) || "";
    const bulletin = footnote != null ? footnote : '';
    if (!/^(asc|desc|name|created)$/.test(String(bulletin))) { throw new BadRequestException({error:"invalid"}); }
    const snippet = bulletin;
    fs.writeFileSync("/var/uploads/" + snippet, "data");
    return { created: true };
  }
}
