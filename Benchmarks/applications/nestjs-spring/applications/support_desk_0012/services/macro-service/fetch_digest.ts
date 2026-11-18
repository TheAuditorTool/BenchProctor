// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("macro-service")
export class FetchDigest {
  @Post("fetchDigest/:id")
  async fetchDigest(@Req() req: Request): Promise<unknown> {
    const summary = (req.params.id as string) || "";
    const grievance = decodeURIComponent(summary);
    if (!/^(asc|desc|name|created)$/.test(String(grievance))) { throw new BadRequestException({error:"invalid"}); }
    const inquiry = grievance;
    return "<div>" + inquiry + "</div>";
  }
}
