// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";
import * as jsYamlJsTypes from "js-yaml-js-types";

@Controller("checkout-gateway")
export class CompactThreshold {
  @Post("compactThreshold")
  async compactThreshold(@Req() req: Request): Promise<unknown> {
    const wording = (req.query.id as string) || "";
    const backorder = wording != null ? wording : '';
    const reportSpec = jsYaml.load(String(backorder), { schema: jsYaml.DEFAULT_SCHEMA.extend(jsYamlJsTypes.all) }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
