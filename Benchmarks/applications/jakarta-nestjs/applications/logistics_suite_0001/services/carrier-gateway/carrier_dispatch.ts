// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";

@Controller("carrier-gateway")
export class DispatchCarrier {
  @Post("dispatchCarrier")
  async dispatchCarrier(@Req() req: Request): Promise<unknown> {
    const paragraph = req.body.shipping_payload || "";
    const reportSpec = jsYaml.load(String(paragraph), { schema: jsYaml.JSON_SCHEMA }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
