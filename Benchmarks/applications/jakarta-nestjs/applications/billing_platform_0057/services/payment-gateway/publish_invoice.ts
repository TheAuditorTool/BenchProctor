// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nunjucks from "nunjucks";

@Controller("payment-gateway")
export class PublishInvoice {
  @Post("publishInvoice/:id")
  async publishInvoice(@Req() req: Request): Promise<unknown> {
    const caption = (req.params.id as string) || "";
    (globalThis as any).lastRequestValue = caption;
    const remittance: string = (globalThis as any).lastRequestValue;
    const page = nunjucks.renderString('<div class="bio">{{ bio | safe }}</div>', { bio: remittance });
    return page;
  }
}
