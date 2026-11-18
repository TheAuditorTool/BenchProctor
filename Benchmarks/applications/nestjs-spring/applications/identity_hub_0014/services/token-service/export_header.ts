// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("token-service")
export class ExportHeader {
  @Post("exportHeader/:id")
  async exportHeader(@Req() req: Request): Promise<unknown> {
    const snippet = (req.params.id as string) || "";
    const persona = decodeURIComponent(snippet);
    if (!/^(asc|desc|name|created)$/.test(String(persona))) { throw new BadRequestException({error:"invalid"}); }
    const synopsis = persona;
    return "<div>" + synopsis + "</div>";
  }
}
