// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("ledger-sync")
export class ValidateHeader {
  @Post("validateHeader")
  async validateHeader(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.body as string) || "";
    const _carrier: { value: string } = { value: '' };
    _carrier.value = synopsis;
    const arrears: string = _carrier.value;
    http.get(arrears);
    return { created: true };
  }
}
