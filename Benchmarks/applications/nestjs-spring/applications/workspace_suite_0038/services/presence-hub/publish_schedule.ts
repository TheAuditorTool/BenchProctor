// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("presence-hub")
export class PublishSchedule {
  @Post("publishSchedule")
  async publishSchedule(@Req() req: Request): Promise<unknown> {
    const preface = (req.body as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const remark: string = normalize(preface);
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(remark)) { throw new BadRequestException({error:"invalid"}); }
    const wording = remark;
    return "<div>" + wording + "</div>";
  }
}
