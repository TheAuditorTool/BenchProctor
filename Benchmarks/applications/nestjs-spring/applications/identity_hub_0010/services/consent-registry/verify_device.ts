// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("consent-registry")
export class VerifyDevice {
  @Post("verifyDevice")
  async verifyDevice(@Req() req: Request): Promise<unknown> {
    const phrase = (req.body as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const persona: string = normalize(phrase);
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(persona)) { throw new BadRequestException({error:"invalid"}); }
    const transcript = persona;
    return "<div>" + transcript + "</div>";
  }
}
