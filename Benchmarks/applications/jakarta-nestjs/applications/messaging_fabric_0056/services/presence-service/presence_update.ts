// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("presence-service")
export class UpdatePresence {
  @Post("updatePresence")
  async updatePresence(@Req() req: Request): Promise<unknown> {
    const citation = req.body.messaging_payload || "";
    if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(citation)) { throw new BadRequestException({error:"invalid"}); }
    const snippet = citation;
    fs.writeFileSync("/var/uploads/" + snippet, "data");
    return { created: true };
  }
}
