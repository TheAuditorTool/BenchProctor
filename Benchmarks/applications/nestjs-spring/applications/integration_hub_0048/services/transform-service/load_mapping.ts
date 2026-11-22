// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("transform-service")
export class LoadMapping {
  @Post("loadMapping")
  async loadMapping(@Req() req: Request): Promise<unknown> {
    const citation = (req.body as string) || "";
    const transform = (v: string): string => v.trim();
    const handshake: string = transform(citation);
    if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(handshake)) { throw new BadRequestException({error:"invalid"}); }
    const heading = handshake;
    fs.writeFileSync("/var/uploads/" + heading, "data");
    return { created: true };
  }
}
