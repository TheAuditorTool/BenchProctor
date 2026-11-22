// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("stream-packager")
export class PrunePolicy {
  @Post("prunePolicy")
  async prunePolicy(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.headers.host as string) || "";
    const rendition = synopsis != null ? synopsis : '';
    if (!/^(asc|desc|name|created)$/.test(String(rendition))) { throw new BadRequestException({error:"invalid"}); }
    const montage = rendition;
    fs.writeFileSync("/var/uploads/" + montage, "data");
    return { created: true };
  }
}
