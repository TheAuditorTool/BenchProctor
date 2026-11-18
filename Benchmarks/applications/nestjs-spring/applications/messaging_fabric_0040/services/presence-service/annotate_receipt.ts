// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("presence-service")
export class AnnotateReceipt {
  @Post("annotateReceipt/:id")
  async annotateReceipt(@Req() req: Request): Promise<unknown> {
    const preface = (req.params.id as string) || "";
    const bulletin = decodeURIComponent(preface);
    if (!/^(asc|desc|name|created)$/.test(String(bulletin))) { throw new BadRequestException({error:"invalid"}); }
    const notice = bulletin;
    return "<div>" + notice + "</div>";
  }
}
