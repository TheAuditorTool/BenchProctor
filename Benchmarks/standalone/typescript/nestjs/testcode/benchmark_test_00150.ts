// SPDX-License-Identifier: Apache-2.0
import { Controller, Headers, Post, Req, BadRequestException } from "@nestjs/common";
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
  @Post("BenchmarkTest00150")
  async BenchmarkTest00150(@Headers("x-forwarded-for") xff: string, @Req() req: Request): Promise<unknown> {
    const userInput = xff || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(userInput);
    const data: string = readInput();
    if (!/^[a-zA-Z0-9 _.\-]+$/.test(data)) { throw new BadRequestException({error:"invalid"}); }
    const processed = data;
    req.session.data = String(processed);
    return { created: true };
  }
}
