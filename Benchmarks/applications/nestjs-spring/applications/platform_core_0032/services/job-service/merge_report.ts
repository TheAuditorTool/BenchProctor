// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("job-service")
export class MergeReport {
  @Post("mergeReport")
  async mergeReport(@Req() req: Request): Promise<unknown> {
    const remark = (req.headers["x-forwarded-for"] as string) || "";
    const persona = remark != null ? remark : '';
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(persona)) { throw new BadRequestException({error:"invalid"}); }
    const handshake = persona;
    return "<div>" + handshake + "</div>";
  }
}
