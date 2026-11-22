// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("knowledge-index")
export class ExportConfig {
  @Post("exportConfig")
  async exportConfig(@Req() req: Request): Promise<unknown> {
    const blurb = (req.headers.referer as string) || "";
    const formData = Object.freeze({ payload: blurb });
    const inquiry = formData.payload;
    if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(inquiry)) { throw new BadRequestException({error:"invalid"}); }
    const grievance = inquiry;
    fs.writeFileSync("/var/uploads/" + grievance, "data");
    return { created: true };
  }
}
