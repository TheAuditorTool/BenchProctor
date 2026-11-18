// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("digest-service")
export class VerifySubscription {
  @Post("verifySubscription/:id")
  async verifySubscription(@Req() req: Request): Promise<unknown> {
    const paragraph = (req.params.id as string) || "";
    const bulletin = decodeURIComponent(paragraph);
    if (!/^(asc|desc|name|created)$/.test(String(bulletin))) { throw new BadRequestException({error:"invalid"}); }
    const synopsis = bulletin;
    return "<div>" + synopsis + "</div>";
  }
}
