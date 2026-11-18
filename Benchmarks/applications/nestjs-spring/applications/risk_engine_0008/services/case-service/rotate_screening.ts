// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("case-service")
export class RotateScreening {
  @Post("rotateScreening/:id")
  async rotateScreening(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.params.id as string) || "";
    const verdict = decodeURIComponent(synopsis);
    if (!/^(asc|desc|name|created)$/.test(String(verdict))) { throw new BadRequestException({error:"invalid"}); }
    const grievance = verdict;
    return "<div>" + grievance + "</div>";
  }
}
