// SPDX-License-Identifier: Apache-2.0
import { Controller, Headers, Post, Req, BadRequestException } from "@nestjs/common";
import { Request, Response } from "express";
import * as zod from "zod";
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";

@Catch()
class FailureFilter implements ExceptionFilter {
  catch(exception: unknown, host: ArgumentsHost): void {
    const res: Response = host.switchToHttp().getResponse();
    const status = exception instanceof HttpException ? exception.getStatus() : 500;
    const body = exception instanceof HttpException ? exception.getResponse() : { error: "internal" };
    res.status(status).json(body);
  }
}

@Controller("benchmark")
@UseFilters(FailureFilter)
export class BenchmarkController {
  @Post("BenchmarkTest00348")
  async BenchmarkTest00348(@Headers("host") host: string, @Req() req: Request): Promise<unknown> {
    const userInput = host || "";
    const data = String(userInput).replace(/\u0000/g, "");
    const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.\-]+$/).safeParse(String(data));
    if (!_parsed.success) { throw new BadRequestException({error:"invalid"}); }
    const processed = _parsed.data;
    req.session.data = String(processed);
    return { created: true };
  }
}
