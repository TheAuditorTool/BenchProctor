// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("mapping-store")
export class PublishConnector {
  @Post("publishConnector")
  async publishConnector(@Req() req: Request): Promise<unknown> {
    const wording = (req.headers.referer as string) || "";
    const formData = Object.freeze({ payload: wording });
    const handshake = formData.payload;
    if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(handshake)) { throw new BadRequestException({error:"invalid"}); }
    const subject = handshake;
    fs.writeFileSync("/var/uploads/" + subject, "data");
    return { created: true };
  }
}
