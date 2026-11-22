// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request, Response } from "express";
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
  @Post("BenchmarkTest00014")
  async BenchmarkTest00014(@Req() req: Request): Promise<unknown> {
    const userInput = process.env.APP_INPUT || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const data: string = normalize(userInput);
    if (!/^[a-zA-Z0-9 _.\-]+$/.test(data)) { throw new BadRequestException({error:"invalid"}); }
    const processed = data;
    Object.assign(req.session, { data: String(processed), expiresAt: Date.now() + 900000 });
    return { created: true };
  }
}
