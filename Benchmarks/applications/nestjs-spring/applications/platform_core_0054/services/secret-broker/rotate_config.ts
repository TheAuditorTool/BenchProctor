// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("secret-broker")
export class RotateConfig {
  @Post("rotateConfig")
  async rotateConfig(@Req() req: Request): Promise<unknown> {
    const snippet = (req.body as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const persona: string = normalize(snippet);
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(persona)) { throw new BadRequestException({error:"invalid"}); }
    const handshake = persona;
    return "<div>" + handshake + "</div>";
  }
}
