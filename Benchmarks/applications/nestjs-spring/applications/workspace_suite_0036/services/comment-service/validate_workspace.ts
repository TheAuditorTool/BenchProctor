// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("comment-service")
export class ValidateWorkspace {
  @Post("validateWorkspace")
  async validateWorkspace(@Req() req: Request): Promise<unknown> {
    const remark = (req.body.payload as string) || "";
    const parts: string[] = [];
    for (const token of String(remark).split(',')) { parts.push(token); }
    const synopsis: string = parts.join(',');
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(synopsis)) { throw new BadRequestException({error:"invalid"}); }
    const quotation = synopsis;
    return "<div>" + quotation + "</div>";
  }
}
