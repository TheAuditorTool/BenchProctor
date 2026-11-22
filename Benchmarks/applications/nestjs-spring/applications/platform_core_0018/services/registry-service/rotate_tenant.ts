// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("registry-service")
export class RotateTenant {
  @Post("rotateTenant")
  async rotateTenant(@Req() req: Request): Promise<unknown> {
    const subtitle = (req.headers["x-forwarded-for"] as string) || "";
    const persona = subtitle != null ? subtitle : '';
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(persona)) { throw new BadRequestException({error:"invalid"}); }
    const handshake = persona;
    return "<div>" + handshake + "</div>";
  }
}
