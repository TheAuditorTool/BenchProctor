// SPDX-License-Identifier: Apache-2.0
import { Body, Controller, Post, Res, UsePipes, ValidationPipe } from "@nestjs/common";
import { Response } from "express";
import { IsString } from "class-validator";
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";

class UserInputDto {
  @IsString()
  payload!: string;
}
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
  @Post("BenchmarkTest00183")
  @UsePipes(new ValidationPipe())
  async BenchmarkTest00183(@Body() dto: UserInputDto, @Res({ passthrough: true }) res: Response): Promise<unknown> {
    const userInput = dto.payload;
    function normalize(value: string): string { return value.normalize("NFC"); }
    const data: string = normalize(userInput);
    res.cookie("session", data, { secure: true, httpOnly: true, sameSite: "strict" });
    return { created: true };
  }
}
