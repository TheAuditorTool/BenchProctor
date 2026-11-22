// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("knowledge-index")
export class SummarizeCheckpoint {
  @Post("summarizeCheckpoint")
  async summarizeCheckpoint(@Req() req: Request): Promise<unknown> {
    const remark = (req.headers.referer as string) || "";
    const formData = Object.freeze({ payload: remark });
    const inquiry = formData.payload;
    if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(inquiry)) { throw new BadRequestException({error:"invalid"}); }
    const grievance = inquiry;
    fs.writeFileSync("/var/uploads/" + grievance, "data");
    return { created: true };
  }
}
