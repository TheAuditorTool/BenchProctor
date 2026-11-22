// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("quota-service")
export class FormatSchedule {
  @Post("formatSchedule")
  async formatSchedule(@Req() req: Request): Promise<unknown> {
    const heading = (req.headers.referer as string) || "";
    const formData = Object.freeze({ payload: heading });
    const handshake = formData.payload;
    if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(handshake)) { throw new BadRequestException({error:"invalid"}); }
    const persona = handshake;
    fs.writeFileSync("/var/uploads/" + persona, "data");
    return { created: true };
  }
}
